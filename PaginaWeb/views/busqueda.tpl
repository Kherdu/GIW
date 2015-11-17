% include('header.tpl', **data)
<form action="/browseByField" method="post">
    <select name="tabla" class="form-control" id="tabla">
        <option value="juego">Juego</option>
        <option value="prestamo">Prestamo</option>
        <option value="usuario">Usuario</option>
    </select><br>
    <label>Campo a buscar</label>
    <div id="campoJuego">
        <div class="radio">
            <label>
                <input type="radio" value="id" name="campoJuego" checked>
                id
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="nombre" name="campoJuego">
                Nombre
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="descripcion" name="campoJuego">
                Descripción
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="disponible" name="campoJuego">
                Disponible
            </label>
        </div>
    </div>
    <div id="campoPrestamo">
        <div class="radio">
            <label>
                <input type="radio" value="id" name="campoPrestamo" checked>
                id
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="fecha_inicio" name="campoPrestamo">
                Fecha inicio
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="nombre" name="campoPrestamo">
                Fecha fin
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="juego_id" name="campoPrestamo">
                Juego id
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="usuario_prestado" name="campoPrestamo">
                Usuario prestado
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="dni_prestado" name="campoPrestamo">
                DNI prestado
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="devuelto" name="campoPrestamo">
                Devuelto
            </label>
        </div>
    </div>
    <div id="campoUsuario">
        <div class="radio">
            <label>
                <input type="radio" value="id" name="campoUsuario" checked>
                id
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="nick" name="campoUsuario">
                Nick
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="nombre" name="campoUsuario">
                Nombre
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" value="dni" name="campoUsuario">
                DNI
            </label>
        </div>
    </div>
    <input placeholder="Introduce la busqueda" name="busqueda" class="form-control"><br>
    <input type="submit" value="Buscar" class="form-control">
</form>
<script>
    $(document).on('ready', function(){
        $("#campoJuego").show();
        $("#campoPrestamo").hide();
        $("#campoUsuario").hide();
        $("#tabla").on('change', function(){
            if($(this).val() == 'juego'){
                $("#campoJuego").show();
                $("#campoPrestamo").hide();
                $("#campoUsuario").hide();
            }else if($(this).val() == 'prestamo'){
                $("#campoJuego").hide();
                $("#campoPrestamo").show();
                $("#campoUsuario").hide();
            }else if($(this).val() == 'usuario'){
                $("#campoJuego").hide();
                $("#campoPrestamo").hide();
                $("#campoUsuario").show();
            }
        });
    });
</script>
% include('footer.tpl')
