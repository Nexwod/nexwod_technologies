# Generated by Django 3.2.21 on 2023-09-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('DT', 'Delta'), ('BR', 'Borno'), ('IM', 'Imo'), ('AK', 'Akwa-ibom'), ('KT', 'Kastina'), ('ZM', 'Zamfara'), ('RV', 'Rivers'), ('JG', 'Jigawa'), ('KG', 'Kogi'), ('KO', 'Kano'), ('EN', 'Enugu'), ('LG', 'Lagos'), ('BY', 'Bayelsa'), ('KN', 'Kano'), ('KB', 'Kebbi'), ('KD', 'Kaduna'), ('BN', 'Benue'), ('CR', 'Cross-River'), ('ON', 'Ondo'), ('KW', 'Kwara'), ('YB', 'Yobe'), ('AD', 'Adamawa'), ('GB', 'Gombe'), ('NG', 'Niger'), ('TB', 'Taraba'), ('BC', 'Bauchi'), ('OY', 'Oyo'), ('EB', 'Ebonyi'), ('AB', 'Abia'), ('AN', 'Anambra'), ('PT', 'Plateau'), ('EK', 'Ekiti'), ('NS', 'Nassarawa'), ('SK', 'Sokoto'), ('ED', 'Edo'), ('OS', 'Osun'), ('OG', 'Ogun')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('On the Way', 'On the Way'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GD', 'Graphic design'), ('WS', 'Web Services'), ('OT', 'Others'), ('PS', 'Printing Services'), ('PF', 'Picture Frames')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('RX', 'Rolex'), ('VS', 'Versace'), ('HR', 'Hermes'), ('DG', 'Dolce and Gabanna'), ('GC', 'Gucci'), ('CK', 'Calvin Klein'), ('LV', 'Louis Vuitton'), ('AD', 'Addidas'), ('GV', 'Givenchy'), ('FL', 'Fila'), ('LC', 'Lacosta'), ('SP', 'Supreme')], max_length=2),
        ),
    ]
