
%include('header.tpl', title='prestamo')

<h1>Añade un prestamo</h1>
% if 'msg' in locals():
<h3>{{msg}}</h3>
%end
<form action="prestamo" method="post">
	<label>Selecciona el juego</label><input type="text" name="juegoPrest"><br>
	<label>Introduce el usuario destinatario del prestamo</label><input type="text" name="personaPrest"><br>
	<label>Descripcion</label><br>
	<label>Disponible</label><br>
</form>

%include('footer.tpl')