// teclas de atalho (hotkeys)
document.addEventListener("keydown", (event) => {
    if (event.target.tagName !== "INPUT" && event.target.tagName !== "TEXTAREA") {
        switch (event.key) {
            case " ":
                togglePlayPause();
                break;
            case "ArrowLeft":
                skipBackward();
                break;
            case "ArrowRight":
                skipForward();
                break;
            case "ArrowUp":
                event.preventDefault(); // Evita o comportamento padrão da tecla de seta para rolar a página
                increaseVolume();
                break;
            case "ArrowDown":
                event.preventDefault(); // Evita o comportamento padrão da tecla de seta para rolar a página
                decreaseVolume();
                break;
            case "f":
                toggleFullScreen();
                break;
            default:
                break;
        }
    }
});

// Adiciona o foco ao elemento de vídeo ao clicar nele
mainVideo.addEventListener("click", () => {
    mainVideo.focus();
});

function togglePlayPause() {
    if (mainVideo.paused) {
        mainVideo.play();
    } else {
        mainVideo.pause();
    }
}

function skipBackward() {
    mainVideo.currentTime -= 15;
}

function skipForward() {
    mainVideo.currentTime += 15;
}

function increaseVolume() {
    if (mainVideo.volume < 1) {
        mainVideo.volume += 0.1;
    }
}

function decreaseVolume() {
    if (mainVideo.volume > 0) {
        mainVideo.volume -= 0.1;
    }
}

function toggleFullScreen() {
    if (!document.fullscreenElement) {
        container.classList.add("fullscreen");
        if (container.requestFullscreen) {
            container.requestFullscreen();
        } else if (container.mozRequestFullScreen) {
            container.mozRequestFullScreen();
        } else if (container.webkitRequestFullscreen) {
            container.webkitRequestFullscreen();
        } else if (container.msRequestFullscreen) {
            container.msRequestFullscreen();
        }
    } else {
        container.classList.remove("fullscreen");
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
    }
}


