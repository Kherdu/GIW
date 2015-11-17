
%include('header.tpl', **data)

<h3>Datos del préstamo</h3>
<form action="/prestamo/{{data["prestamo"]["id"]}}/editar" method="post" class="form-horizontal">
    <div class="form-group">
      <label class="col-sm-2">Juego</label>
      <div class="col-sm-4">
        <input value="{{data["prestamo"]["juego_id"]}}" name="juegoPrest" type="hidden">
        
        <a href="/juego/{{data["prestamo"]["juego_id"]}}">{{data["prestamo"]["juego_id"]}}</a>
      </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2">Prestado a</label>
        <div class="col-sm-4">
          <input value="{{data["prestamo"]["usuario_prestado"]}}" name="personaPrest" type="text" class="form-control" placeholder="Introduce el nombre a quiens se presta el juego">
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2">DNI</label>
        <div class="col-sm-4">
          <input value="{{data["prestamo"]["dni_prestado"]}}" name="dniPrest" type="text" class="form-control" placeholder="Introduce el nombre a quiens se presta el juego">
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2">Fecha de inicio</label>
        <div class="col-sm-4">
          <input value="{{data["prestamo"]["fecha_inicio"]}}" name="fecha_inicio" type="date" class="form-control" placeholder="Introduce el nombre del juego">
        </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Fecha de fin</label>
      <div class="col-sm-4">
          <input value="{{data["prestamo"]["fecha_fin"]}}" name="fecha_fin" type="date" class="form-control" placeholder="Introduce el nombre del juego">
        </div>
    </div>
    <div class="form-group">
      <label class="col-sm-2">Devuelto</label>
      <div class="col-sm-4">
        % if data["prestamo"]["devuelto"] == 1:
            <label class="radio-inline">
              <input type="radio" name="devuelto" value="1" checked> Sí
            </label>
            <label class="radio-inline">
              <input type="radio" name="devuelto" value="0"> No
            </label>
        % else:
            <label class="radio-inline">
              <input type="radio" name="devuelto" value="1"> Sí
            </label>
            <label class="radio-inline">
              <input type="radio" name="devuelto" value="0" checked> No
            </label>
        %end
      </div>
    </div>
    <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
      <button type="submit" class="btn btn-default">Modificar préstamo</button>
    </div>
  </div>
    <div class="form-group">
    <div class="col-sm-offset-2 col-sm-4">
        <a class="btn btn-danger" href="/prestamo/{{data["prestamo"]["id"]}}/eliminar">Eliminar préstamo</a>
    </div>
    </div>
</form>


%include('footer.tpl')