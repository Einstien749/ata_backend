from django.db import models

# Create your models here.

class Portfolio(models.Model):
    risk_score = models.PositiveIntegerField()

    nigerian_stocks = models.PositiveIntegerField()

    foriegn_stocks = models.PositiveIntegerField()

    tech_stocks = models.PositiveIntegerField()

    emerging_stocks = models.PositiveIntegerField()

    nigerian_bonds = models.PositiveIntegerField()

    foriegn_bonds = models.PositiveIntegerField()

    commodities = models.PositiveIntegerField()

    real_estate = models.PositiveIntegerField()

    t_bills = models.PositiveIntegerField()

    alternative = models.PositiveIntegerField()

    class Meta:
        
        # Specify the MongoDB collection name
        db_table = 'portfolio'
        # Optionally, specify the database name
        app_label = 'odimayo_ata_database'
