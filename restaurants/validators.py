from django.core.exceptions import ValidationError

CATEGORIES = ['American', 'Fusion']

def validate_category(value):
	cap = value.capitalize()
	if not value in CATEGORIES and not cap in CATEGORIES:
		raise ValidationError(f"{value} is not a valid category")