# Generated by Django 4.0.2 on 2022-04-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneStorage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chromosome', models.CharField(max_length=10)),
                ('start_pos', models.IntegerField()),
                ('end_pos', models.IntegerField()),
                ('observed', models.TextField()),
                ('reference', models.TextField(blank=True, default=None, null=True)),
                ('zygosity', models.TextField(default=None)),
                ('refGene_function', models.TextField(blank=True, default=None, null=True)),
                ('refGene_gene', models.TextField()),
                ('quality', models.TextField(blank=True, default=None, null=True)),
                ('refGene_exonic_function', models.TextField(blank=True, default=None, null=True)),
                ('AC', models.TextField(blank=True, default=None, null=True)),
                ('AC_hom', models.TextField(blank=True, default=None, null=True)),
                ('aug_all', models.TextField(blank=True, default=None, null=True)),
                ('ExAC_ALL', models.TextField(blank=True, default=None, null=True)),
                ('gnomAD_exome_AF', models.TextField(blank=True, default=None, null=True)),
                ('Kaviar_AF', models.TextField(blank=True, default=None, null=True)),
                ('SIFT_pred_41a', models.TextField(blank=True, default=None, null=True)),
                ('SIFT4G_pred_41a', models.TextField(blank=True, default=None, null=True)),
                ('Polyphen2_HDIV_pred_41a', models.TextField(blank=True, default=None, null=True)),
                ('Polyphen2_HVAR_pred_41a', models.TextField(blank=True, default=None, null=True)),
                ('CADD_phred_41a', models.TextField(blank=True, default=None, null=True)),
                ('CLNSIG', models.TextField(blank=True, default=None, null=True)),
                ('filename', models.TextField(blank=True, default=None, null=True)),
                ('count_hom', models.IntegerField(blank=True, default=None, null=True)),
                ('count_het', models.IntegerField(blank=True, default=None, null=True)),
                ('count_total', models.IntegerField(blank=True, default=None, null=True)),
                ('files_uploaded', models.IntegerField(blank=True, default=None, null=True)),
                ('New_allele_frequency', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
