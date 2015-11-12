
% include('header.tpl', data={'title': 'Login', 'userType': data["userType"]})

<h1>Login</h1>
% if 'data' in locals() and msg in data:
<h3>{{data["msg"]}}</h3>
%end
<form action="login" method="post">
    <label>Usuario</label><input type="text" name="user"><br>
	<label>Contraseña</label><input type="password" name="password"><br>
	<input type="submit" value="Entrar">
</form>
<p>¿No estás registrado? pincha <a href="registro">aqui</a> para registrarte</p>
% include('footer.tpl')
