from django.db import models
from custom_auth.models import CustomUser

class Customer(models.Model):
    # Basic business details
    status_choices = [
        ("proprietor", "Proprietor"),
        ("firm", "Firm"),
        ("private_limited", "Private Limited"), 
        ("public_limited", "Public Limited"), 
        ("bank", "Bank"),
        ("aop_or_boi", "AOP Or BOI"), 
        ("huf", "HUF"),
        ("ajp", "AJP"),
        ("society", "Society"),
        ("individual", "Individual"),
    ]
    DCS_CHOICES = [("new_dcs", "New DCS"), 
                   ("received", "Received"), 
                   ("not_received", "Not Received"),
                   ("na", "NA")]

    name_of_business = models.CharField(max_length=255)
    file_no = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.CharField(max_length=50, unique=True)
    business_pan_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(choices=status_choices, max_length=50, blank=True, null=True)

    # Address fields
    address = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)

    # Contact details
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    additional_contact_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_email_id = models.EmailField(blank=True, null=True)

    # GST and registration fields
    destination_address = models.CharField(max_length=200, blank=True, null=True)
    gst_no = models.CharField(max_length=400, blank=True, null=True)
    gst_state_code = models.CharField(max_length=10, blank=True, null=True)
    cin_number = models.CharField(max_length=50, blank=True, null=True)
    llipin_number = models.CharField(max_length=50, blank=True, null=True)
    din_number = models.CharField(max_length=50, blank=True, null=True)

    # Personal details
    date_of_birth = models.DateField(blank=True, null=True)
    pan_no = models.CharField(max_length=50, blank=True, null=True)

    # Account management
    enable_account = models.BooleanField(default=True)
    accountant_name = models.CharField(max_length=100, blank=True, null=True)
    accountant_phone = models.CharField(max_length=100, blank=True, null=True)
    dsc = models.CharField(choices=DCS_CHOICES, default="na", max_length=50, null=True, blank=True)

    # Metadata
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_created_by")
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_updated_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_of_business} ({self.customer_code})"


class CustomerContacts(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_contact")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_contact_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_contact_updated_by")
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} ({self.designation})"


class CustomerGroups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_group_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_group_updated_by")
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class CustomerGroupMapping(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_group_mapping")
    group = models.ForeignKey(CustomerGroups, on_delete=models.CASCADE, related_name="customer_group_mapping")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_group_mapping_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_group_mapping_updated_by")
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer} ({self.group.name})"
    

class CustomerBranch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_branch_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_branch_updated_by")
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    

class CustomerBranchMapping(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_branch_mapping")
    branch = models.ForeignKey(CustomerBranch, on_delete=models.CASCADE, related_name="customer_branch_mapping")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_branch_mapping_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="customer_branch_mapping_updated_by")
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer} ({self.branch.name})"
