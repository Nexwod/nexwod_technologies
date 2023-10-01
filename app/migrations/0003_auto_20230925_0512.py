# Generated by Django 3.2.21 on 2023-09-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230925_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('PT', 'Plateau'), ('LG', 'Lagos'), ('RV', 'Rivers'), ('KO', 'Kano'), ('KG', 'Kogi'), ('AD', 'Adamawa'), ('EK', 'Ekiti'), ('YB', 'Yobe'), ('NG', 'Niger'), ('KN', 'Kano'), ('GB', 'Gombe'), ('BC', 'Bauchi'), ('ED', 'Edo'), ('AN', 'Anambra'), ('NS', 'Nassarawa'), ('ON', 'Ondo'), ('TB', 'Taraba'), ('KT', 'Kastina'), ('IM', 'Imo'), ('CR', 'Cross-River'), ('OG', 'Ogun'), ('KB', 'Kebbi'), ('JG', 'Jigawa'), ('OS', 'Osun'), ('AB', 'Abia'), ('BN', 'Benue'), ('DT', 'Delta'), ('BR', 'Borno'), ('OY', 'Oyo'), ('SK', 'Sokoto'), ('KD', 'Kaduna'), ('AK', 'Akwa-ibom'), ('EB', 'Ebonyi'), ('KW', 'Kwara'), ('BY', 'Bayelsa'), ('ZM', 'Zamfara'), ('EN', 'Enugu')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On the Way', 'On the Way'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('OT', 'Others'), ('PS', 'Printing Services'), ('GD', 'Graphic design'), ('WS', 'Web Services'), ('PF', 'Picture Frames')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('LV', 'Louis Vuitton'), ('AD', 'Addidas'), ('RX', 'Rolex'), ('CK', 'Calvin Klein'), ('FL', 'Fila'), ('DG', 'Dolce and Gabanna'), ('GV', 'Givenchy'), ('SP', 'Supreme'), ('GC', 'Gucci'), ('HR', 'Hermes'), ('LC', 'Lacosta'), ('VS', 'Versace')], max_length=2),
        ),
    ]