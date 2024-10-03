document.getElementById('botao-pesquisa').addEventListener('click', function() {
    var campoPesquisa = document.getElementById('campo-pesquisa');
    console.log(campoPesquisa, '11111111')
    if (campoPesquisa.style.display === 'none'){
        campoPesquisa.style.display = 'flex'
    } else{
        campoPesquisa.style.display = 'none'
    }

});
