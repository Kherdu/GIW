%include('header.tpl', **data)

<table class="table table-hover">
<thead>
    <tr>
        <th>Id</th>
        <th>Nombre</th>
        <th>Descripción</th>
        <th>Disponible</th>
        <th>Eliminar</th>
    </tr>
</thead>
% for juego in data["juegos"]:
   
    <tr>
        <td><a href="/juego/{{juego["id"]}}"> {{juego["id"]}}</a></td>
        <td><strong>{{juego["nombre"]}}</strong></td>
        <td>{{juego["descripcion"]}}</td>
        <td>{{juego["disponible"]}}</td>
        <td><a href="/juego/{{juego["id"]}}/eliminar"><span class="text-danger">Eliminar</span></a></td>
    </tr> 

% end

</table>
<h3>Añadir juego</h3>
<form action="juego" method="post" class="form-horizontal">
    <div class="form-group">
        <label class="col-sm-2">Nombre del juego</label>
        <div class="col-sm-4">
          <input name="nombre" type="text" class="form-control" placeholder="Introduce el nombre del juego">
        </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Descripción</label>
      <div class="col-sm-4">
        <textarea name="descripcion" class="form-control" placeholder="Introduce la descripción del juego"></textarea>
      </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Disponible</label>
      <div class="col-sm-4">
        <label class="radio-inline">
          <input type="radio" name="disponible" value="1"> Sí
        </label>
        <label class="radio-inline">
          <input type="radio" name="disponible" value="0"> No
        </label>
      </div>
    </div>
    <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
      <button type="submit" class="btn btn-default">Entrar</button>
    </div>
  </div>
</form>

%include('footer.tpl')