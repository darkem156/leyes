from rest_framework import serializers
from .models import Ley, Tema, Historial, Decreto

class DecretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decreto
        fields = ['id', 'numero', 'external_id']  # external_id opcional

class HistorialSerializer(serializers.ModelSerializer):
    decretos = DecretoSerializer(many=True)
    rutaArchivo = serializers.CharField()

    class Meta:
        model = Historial
        fields = ['id', 'fecha_ppo', 'rutaArchivo', 'comentario', 'estatus', 'activo', 'decretos']

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = ['id', 'tema']

class LeySerializer(serializers.ModelSerializer):
    tema = TemaSerializer(many=True)
    historial = HistorialSerializer(many=True)

    class Meta:
        model = Ley
        fields = ['id', 'titulo', 'abrogada', 'comentario', 'tema', 'historial']

    def create(self, validated_data):
        tema_data = validated_data.pop('tema', [])
        historial_data = validated_data.pop('historial', [])

        ley = Ley.objects.create(**validated_data)

        for tema_item in tema_data:
            external_id = tema_item.get('id')
            nombre = tema_item.get('tema')

            if external_id:
                tema_obj, _ = Tema.objects.get_or_create(
                    external_id=external_id,
                    defaults={'tema': nombre}
                )
            else:
                tema_obj, _ = Tema.objects.get_or_create(tema=nombre)

            ley.tema.add(tema_obj)

        for hist_item in historial_data:
            decretos_data = hist_item.pop('decretos', [])
            historial = Historial.objects.create(ley=ley, **hist_item)

            for dec_item in decretos_data:
                dec_external_id = dec_item.get('id')
                numero = dec_item.get('numero')

                if dec_external_id:
                    decreto, _ = Decreto.objects.get_or_create(
                        external_id=dec_external_id,
                        defaults={'numero': numero}
                    )
                else:
                    decreto, _ = Decreto.objects.get_or_create(numero=numero)

                historial.decretos.add(decreto)

        return ley
