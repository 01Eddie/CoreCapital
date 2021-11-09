// function myFunction () {
  // $.ajax({
  // 		type: 'POST',  // Envío con método POST
  // 		url: './question_options',  // Fichero destino (el PHP que trata los datos)
  // 		data: { nom: pnom, pass: ppass } // Datos que se envían
  // 		}).done(function( msg ) {  // Función que se ejecuta si todo ha ido bien
  // 			$("#consola").html(msg);  // Escribimos en el div consola el mensaje devuelto
  // 		}).fail(function (jqXHR, textStatus, errorThrown){ // Función que se ejecuta si algo ha ido mal
  // 		// Mostramos en consola el mensaje con el error que se ha producido
  // 		$("#consola").html("The following error occured: "+ textStatus +" "+ errorThrown);
  // 		});
  // console.log('click');
// }

//{ /* document.getElementsByClassName("botones").onclick = function() {myFunction()}; */ }
// $('.botones').click(myFunction);


const Parrafo = createElement('p', { class: 'mi_parrafo' });

// const Header = createElement('header', { class: 'main-header' }, [Logo, Nav]);

const Parrafo = createElement('p', { class: 'mi_parrafo' });
render(Parrafo, document.getElementById('root'));
