<!-- Sidebar -->
<div id="sidebar-wrapper">

    <ul class="sidebar-nav">
    
        <li class="sidebar-brand">
            <a href="#">
                Préstamo de juegos
            </a>
        </li>
        % if data["userType"] == 'logged':
        <li>
            <a href="/juegos">Juegos</a>
        </li>
        <li>
            <a href="/prestamos">Préstamos</a>
        </li>
        <li>
            <a href="/buscar">Buscar</a>
        </li>
        <li>
            <a href="/logout"><span class="text-danger">Salir</span></a>
        </li>
        % end
    </ul>
</div>
<!-- /#sidebar-wrapper -->