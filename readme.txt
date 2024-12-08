La página principal del proyecto 'LaundryERP' cuenta con un mensaje de bienvenida, descripción y con botones de acceso a las distintas funcionalidades del sistema de gestión de lavanderías.

Sólo le es posible acceder a cada una de estas funcionalidades a los usuarios registrados (sino lo está mostrará una página con un mensaje de error) y este acceso es condicionado de acuerdo a las restricciones de su rol (administrador o empleado).

Existe creado un 'superusuario' el cual tiene acceso al panel adminstrativo de Django cuyas credenciales son:
usuario: admin
contraseña: admin

Adicionalmente este superusuario puede crear usuarios (administradores y/o empleados) directamente desde el panel administrativo, asi como 'prendas', características de los servicios y precios de éstos.

El usuario con el rol de administrador:
- Tiene acceso a la página de Empleados la cual posee una lista de ellos y puede crear usuarios (administradores y/o empleados) desde el formulario de la página/navegador.
- Tiene acceso a la página de Reportes, para generar Reportes de Ventas con filtros e Historial de Clientes que muestran las ventas por cliente y si éste posee ordenes de servicio aún no completadas.
- Tiene acceso a la página de Ventas donde figuran todas las ordenes de servicio completadas(pagadas) y puede obtener el detalle de cada una, así como acceder a editar o eliminar cada una de las mismas.
- Tiene acceso a la página de Clientes donde adicionalmente puede crear nuevos registros de ellos.
- Tiene acceso a la página de Ordenes donde puede listar, editar o eliminar cada una así como tambien registrar como ventas las ordenes que cambien al estado de 'Completada'

El usuario con el rol de empleado:
- No tiene acceso a la página de Empleados ni sus registros.
- Tiene acceso a la página de Reportes y sus funcionalidades.
- Tiene acceso a la página de Ventas donde puede ver el listado, detalles y acceso a editar, pero no puede eliminar.
- Tiene acceso a la página de Clientes pero no puede agregar nuevos datos/clientes.
- Tiene acceso a la página de Ordenes con sus funcionalidades completas.

Para este proyecto se precargaron una lista de 6 clientes, 2 usuarios con rol 'empleado' y un usuario con rol de 'administrador'.

Sus credenciales son:

Empleados:

Rosa Rivas
usuario: rosa@gmail.com
contraseña:123456#$

Pablo Quintana
usuario: pablo@gmail.com
contraseña:123456#$

Administrador:

Evelin Garcia
usuario: evelingarcia@gmail.com
contraseña:123456#$




