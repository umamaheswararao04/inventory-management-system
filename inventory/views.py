from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django import forms

from .models import Product, StockHistory, Category, Supplier
from .forms import ProductForm


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()
    low_stock_products = Product.objects.filter(quantity__lt=10)

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_suppliers': total_suppliers,
        'low_stock_products': low_stock_products,
    }
    return render(request, 'inventory/dashboard.html', context)


# ---------------- PRODUCT LIST ----------------
@login_required
def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q')

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'inventory/product_list.html', {'products': products})


# ---------------- PRODUCT CREATE (ADMIN ONLY) ----------------
@login_required
@permission_required('inventory.add_product', raise_exception=True)
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'inventory/product_form.html', {'form': form})


# ---------------- PRODUCT UPDATE (ADMIN ONLY) ----------------
@login_required
@permission_required('inventory.change_product', raise_exception=True)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/product_form.html', {'form': form})


# ---------------- PRODUCT DELETE (ADMIN ONLY) ----------------
@login_required
@permission_required('inventory.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('product_list')

    return HttpResponseForbidden("Delete not allowed")


# ---------------- STOCK IN (ADMIN + STAFF) ----------------
@login_required
def stock_in(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        qty = int(request.POST.get('quantity', 0))

        if qty > 0:
            prev_qty = product.quantity
            product.quantity += qty
            product.save()

            StockHistory.objects.create(
                product=product,
                change_type='IN',
                quantity_changed=qty,
                previous_quantity=prev_qty,
                new_quantity=product.quantity,
                updated_by=request.user
            )

            messages.success(request, "Stock added successfully!")
            return redirect('product_list')

        messages.error(request, "Invalid quantity")

    return render(request, 'inventory/stock_in.html', {'product': product})


# ---------------- STOCK OUT (ADMIN + STAFF) ----------------
@login_required
def stock_out(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        qty = int(request.POST.get('quantity', 0))

        if 0 < qty <= product.quantity:
            prev_qty = product.quantity
            product.quantity -= qty
            product.save()

            StockHistory.objects.create(
                product=product,
                change_type='OUT',
                quantity_changed=qty,
                previous_quantity=prev_qty,
                new_quantity=product.quantity,
                updated_by=request.user
            )

            messages.success(request, "Stock reduced successfully!")
            return redirect('product_list')

        messages.error(request, "Invalid quantity")

    return render(request, 'inventory/stock_out.html', {'product': product})


# ---------------- CATEGORY & SUPPLIER FORMS ----------------
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address']


# ---------------- CATEGORY CREATE (ADMIN ONLY) ----------------
@login_required
@permission_required('inventory.add_category', raise_exception=True)
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('product_create')
    else:
        form = CategoryForm()

    return render(
        request,
        'inventory/simple_form.html',
        {'form': form, 'title': 'Add Category'}
    )


# ---------------- SUPPLIER CREATE (ADMIN ONLY) ----------------
@login_required
@permission_required('inventory.add_supplier', raise_exception=True)
def supplier_create(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier added successfully!")
            return redirect('product_create')
    else:
        form = SupplierForm()

    return render(
        request,
        'inventory/simple_form.html',
        {'form': form, 'title': 'Add Supplier'}
    )


# ---------------- STOCK HISTORY ----------------
@login_required
def stock_history_view(request):
    histories = StockHistory.objects.select_related(
        'product', 'updated_by'
    ).order_by('-timestamp')

    return render(
        request,
        'inventory/stock_history.html',
        {'histories': histories}
    )
