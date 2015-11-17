%include('header.tpl', **data)
<ol class="breadcrumb">
  <li><a href="/">Inicio</a></li>
  <li class="active">Registro</li>
</ol>
<form class="form-horizontal" action="registro" method="post">
  <div class="form-group">
    <label class="col-sm-2">Nombre de usuario</label>
    <div class="col-sm-4">
      <input name="user" type="text" class="form-control" placeholder="Introduce tu nombre de usuario">
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2">Contraseña</label>
    <div class="col-sm-4">
      <input name="password" type="password" class="form-control" placeholder="Introduce tu contraseña">
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2">Repite la contraseña</label>
    <div class="col-sm-4">
      <input name="password2" type="password" class="form-control" placeholder="Repite la contraseña">
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2">Nombre real</label>
    <div class="col-sm-4">
      <input name="name" type="text" class="form-control" placeholder="Introduce tu nombe real">
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2">DNI</label>
    <div class="col-sm-4">
      <input name="dni" type="text" class="form-control" placeholder="Introduce tu dni">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
      <button type="submit" class="btn btn-default">Registrar</button>
    </div>
  </div>
</form>

%include('footer.tpl')