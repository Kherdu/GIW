
%include('header.tpl', title='juego')

<h1>Añade un juego</h1>
% if 'msg' in locals():
<h3>{{msg}}</h3>
%end
<form action="juego" method="post">
	<label>Nombre del juego</label><input type="text" name="nombre"><br>
	<label>Descripcion</label><input type="password" name="descripcion"><br>
	<label>Disponible</label><input type="text" name="disponible"><br>
</form>
<--  -->
<h1>Modifica un juego</h1>
% if 'msg' in locals():
<h3>{{msg}}</h3>
%end
<form action="juego" method="post">
	<label>Nombre del juego</label><input type="text" value={{}}  name="nombre"><br>
	<label>Descripcion</label><input type="password" value={{}} name="descripcion"><br>
	<label>Disponible</label><input type="text" value={{}} name="disponible"><br>
</form>

%include('footer.tpl')