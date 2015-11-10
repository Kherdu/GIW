
%include('header.tpl', title='Registro')

<h1>Registrate</h1>
<form action="registro" method="post">
	% if msg != '':
		<h3>{{msg}}</h3>
	% end
	<label>Nombre de usuario</label><input type="text" name="user"><br>
	<label>Contraseña</label><input type="password" name="password"><br>
	<label>Repite la contraseña</label><input type="password" name="password2"><br>
	<label>Nombre real</label><input type="text" name="name"><br>
	<label>DNI</label><input type="text" name="dni"><br>
	<input type="submit" value="Entrar">
</form>

%include('footer.tpl')