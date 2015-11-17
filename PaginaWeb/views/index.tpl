
% include('header.tpl', **data)

<form class="form-horizontal" action="login" method="post">
  <div class="form-group">
    <label class="col-sm-1">Usuario</label>
    <div class="col-sm-4">
      <input name="user" type="text" class="form-control" placeholder="Introduce tu nombre de usuario">
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-1">Password</label>
    <div class="col-sm-4">
      <input name="password" type="password" class="form-control" placeholder="Introduce tu contraseña">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-1 col-sm-4">
      <button type="submit" class="btn btn-default">Entrar</button>
    </div>
  </div>
</form>
<p>¿No estás registrado? pincha <a href="registro">aqui</a> para registrarte</p>

% include('footer.tpl')
