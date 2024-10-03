import subprocess
import os

def split_video_and_save_chunks(instance, input_file, output_dir, chunk_duration=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sanitizando o título para uso nos nomes dos chunks a partir de VideoDetails
    if instance.movie:
        safe_title = instance.movie.name_movie.replace(" ", "_").lower()
    else:
        # Caso o título não esteja disponível por algum motivo, usar um padrão
        safe_title = f"video_{instance.id}"

    # Comando FFmpeg para gerar os arquivos .m3u8 e os segmentos .ts
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',  # Codec de vídeo
        '-crf', '18',       # Valor de CRF para boa qualidade (quanto menor o valor, maior a qualidade)
        '-c:a', 'aac',      # Codec de áudio (AAC é amplamente suportado)
        '-b:a', '128k',     # Taxa de bits do áudio
        '-ac', '2',         # Forçar áudio estéreo
        '-f', 'hls',        # Formato HLS
        '-hls_time', str(chunk_duration),  # Duração dos chunks
        '-hls_flags', 'split_by_time',     # Garantir cortes exatos no tempo especificado
        '-hls_playlist_type', 'vod',       # Playlist do tipo VOD (Video on Demand)
        '-hls_segment_filename', os.path.join(output_dir, f'{safe_title}_chunk%03d.ts'),  # Nome dos chunks baseado no título
        os.path.join(output_dir, 'output.m3u8')  # Arquivo de saída .m3u8
    ]

    subprocess.run(command, check=True)