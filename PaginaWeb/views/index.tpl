
% include('header.tpl', title='Login')

<h1>Entra</h1>
<form>
	% if msg != '':
		<h3>{{msg}}</h3>
	% end
	<label>Usuario</label><input type="text" name="user"><br>
	<label>Contraseña</label><input type="password" name="password"><br>
	<input type="submit" value="Entrar">
</form>
<p>¿No estás registrado? pincha <a href="registro">aqui</a> para registrarte</p>

% include('footer.tpl')