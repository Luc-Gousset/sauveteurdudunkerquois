# Generated by Django 3.2.9 on 2021-12-02 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Titre', models.CharField(max_length=200)),
                ('Source', models.TextField()),
                ('Texte', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/sauvetages/')),
            ],
        ),
        migrations.CreateModel(
            name='Recompense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images/Recompenses')),
                ('Nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypeBateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeDuBateau', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Sauvetage',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.article')),
                ('NbMort', models.PositiveIntegerField(default=0)),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.article')),
                ('nbPersonneSauve', models.PositiveIntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.images')),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200)),
                ('Prenom', models.CharField(max_length=200)),
                ('Type', models.CharField(choices=[('Sauveteur', 'Sauveteur'), ('Mecanicien', 'Mecanicien'), ('Capitaine', 'Capitaine')], max_length=15)),
                ('Recompenses', models.ManyToManyField(to='main.Recompense')),
                ('sauvetage', models.ManyToManyField(to='main.Sauvetage')),
            ],
        ),
        migrations.CreateModel(
            name='Bateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200)),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typebateau')),
                ('Sauvetage', models.ManyToManyField(to='main.Sauvetage')),
            ],
        ),
    ]