from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from .models import FilmeVideo
from .chunks import split_video_and_save_chunks


@receiver(post_save, sender=FilmeVideo)
def create_video_chunks(sender, instance, created, **kwargs):
    if created and instance.file:  # Verifica se o arquivo de vídeo está presente
        # Localizando o arquivo de vídeo no sistema de arquivos
        video_path = default_storage.path(instance.file.name)

        # Verifica se o VideoDetails existe
        if instance.movie:
            # Sanitizando o título para uso no nome dos arquivos (remover espaços e caracteres inválidos)
            safe_title = instance.movie.name_movie.replace(" ", "_").lower()

            # Diretório de saída para os chunks
            output_dir = f'media/chunks/movies/{safe_title}/'

            # Gerando os chunks do vídeo
            split_video_and_save_chunks(instance, video_path, output_dir, chunk_duration=30)

            # Atualizando o hls_url no VideoDetails após gerar os chunks
            instance.movie.hls_url = f'/media/chunks/movies/{safe_title}/output.m3u8'
            instance.movie.save()