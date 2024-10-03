// // Funcionando sem Gargalo
// var offcanvasElement = document.getElementById('offcanvasNavbar');
// var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
// var lastBackdrop = null;

// var backdropHandler = function () {
//     var backdrops = document.querySelectorAll('.offcanvas-backdrop');

//     // Remover todos os backdrops, exceto o último
//     for (var i = 0; i < backdrops.length - 1; i++) {
//         backdrops[i].remove();
//     }

//     // Atualizar a referência ao último backdrop
//     lastBackdrop = backdrops.length > 0 ? backdrops[backdrops.length - 1] : null;
// };

// // Remover backdrops extras antes de abrir o offcanvas
// backdropHandler();

// offcanvasElement.addEventListener('show.bs.offcanvas', function () {
//     // Atualizar novamente os backdrops antes de abrir o offcanvas
//     backdropHandler();
// });

// offcanvasElement.addEventListener('hidden.bs.offcanvas', function () {
//     // Remover o último backdrop ao fechar o offcanvas
//     if (lastBackdrop !== null) {
//         lastBackdrop.remove();
//         lastBackdrop = null;
//     }
// });


// // Para não bugar o scroll para baixo
// var offcanvasElement = document.getElementById('offcanvasNavbar');
// var offcanvas = new bootstrap.Offcanvas(offcanvasElement);

// offcanvasElement.addEventListener('hidden.bs.offcanvas', function () {
//     // Restaurar a capacidade de scroll na página principal
//     document.body.style.overflow = 'auto';
// });



  
  
  
  
  
