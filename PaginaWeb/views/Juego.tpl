%include('header.tpl', **data)

<h3>Préstamos del juego</h3>
% if len(data["prestamos"]) > 0:
    <table class="table table-hover">
    <thead>
        <tr>
            <th>Id</th>
            <th>Fecha inicio</th>
            <th>Fecha fin</th>
            <th>Prestado a</th>
            <th>DNI</th>
            <th>Disponible</th>
            <th>Eliminar</th>
        </tr>
    </thead>
    % for prestamo in data["prestamos"]:
        <tr>
        <td><a href="/prestamo/{{prestamo["id"]}}"> {{prestamo["id"]}}</a></td>
        <td>{{prestamo["fecha_inicio"]}}</td>
        <td>{{prestamo["fecha_fin"]}}</td>
        <td>{{prestamo["usuario_prestado"]}}</td>
        <td>{{prestamo["dni_prestado"]}}</td>
        <td>{{prestamo["devuelto"]}}</td>
        <td><a href="/prestamo/{{prestamo["id"]}}/eliminar"><span class="text-danger">Eliminar</span></a></td>
    </tr> 
    % end
    </table>
% else:
    <p class="text-muted">Este juego no tiene préstamos</p>
% end

<h3>Datos del juego</h3>
<form action="/juego/{{data["juego"][0]["id"]}}/editar" method="post" class="form-horizontal">
    <div class="form-group">
        <label class="col-sm-2">Nombre del juego</label>
        <div class="col-sm-4">
          <input value="{{data["juego"][0]["nombre"]}}" name="nombre" type="text" class="form-control" placeholder="Introduce el nombre del juego">
        </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Descripción</label>
      <div class="col-sm-4">
        <textarea name="descripcion" class="form-control" placeholder="Introduce la descripción del juego">{{data["juego"][0]["descripcion"]}}</textarea>
      </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Disponible</label>
      <div class="col-sm-4">
        % if data["juego"][0]["disponible"] == 1:
            <label class="radio-inline">
              <input type="radio" name="disponible" value="1" checked> Sí
            </label>
            <label class="radio-inline">
              <input type="radio" name="disponible" value="0"> No
            </label>
        % else:
            <label class="radio-inline">
              <input type="radio" name="disponible" value="1"> Sí
            </label>
            <label class="radio-inline">
              <input type="radio" name="disponible" value="0" checked> No
            </label>
        %end
      </div>
    </div>
    <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
      <button type="submit" class="btn btn-default">Modificar juego</button>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
        <a class="btn btn-danger" href="/juego/{{data["juego"][0]["id"]}}/eliminar">Eliminar juego</a>
    </div>
    </div>
</form>
%include('footer.tpl')