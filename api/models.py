from django.db import models

class ScrappedItems(models.Model):
	id = models.BigAutoField(primary_key=True)
	adresse = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	prix = models.CharField(max_length=50)
	type_habitat = models.CharField(max_length=50)
	surface_habitable = models.CharField(max_length=50)
	surface_terrain = models.CharField(max_length=50)
	nbr_pieces = models.CharField(max_length=50)
	description = models.TextField()
	dpe = models.CharField(max_length=5)
	ges = models.CharField(max_length=5)
	images = models.JSONField()
	html_content = models.TextField()







