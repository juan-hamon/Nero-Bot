# **Nero-Bot**
Este repositorio contiene el código para este bot de discord, Nero.
## **Funcionalidades**
Nero cuenta con las siguientes funcionalidades:
- Comandos básicos:
  - `$ping`: Hacer ping a Nero para saber el tiempo de respuesta.
  - `$hello`: Saludar a Nero y recibir una respuesta.
  - `$shutdown`: Apagar a Nero (esto solo lo puede hacer el administrador del servidor).
- Comandos de juegos:
  - `$roll`: Nero retorna un número aleatorio del 1 al 100.
- Comandos de ayuda:
  - `$help`: Nero responde de dos formas ante el comando de ayuda:
    - Si se envía el nombre de un comando específico, Nero muestra la descripción de dicho comando junto con los parametros necesarios para utilizarlo.
    - Si no se envía un nombre de comando, Nero Muestra una lista de todos los comandos disponibles, cada uno con su descripción y los parámetros necesarios para utilizarlo.
- Comandos de información:
    - `$userinfo`: Despliega información del usuario mencionado junto al comando. En caso de no mencionar a alguien, Nero despliega la información de quien utilizó el comando.
    - `$serverinfo`: Despliega información del servidor.
- Comandos de moderación:
    - `$kick`: Nero expulsa del servidor a los miembros mencionados junto al comando, se puede anexar una razón de la expulsión.
    - `$ban`: Nero banea del servidor a los miembros mencionados junto al comando, se puede anexar una razón del baneo.
    - `$unban`: Nero elimina el ban de los miembros mencionados junto al comando (se puede utilizar sus ID's o sus nombres de usuario), se puede anexar una razón de la expulsión.
    - `$clear`: Nero elimina cierta cantidad de mensajes en un canal de texto.
- Acciones en el servidor:
    - Nero saluda y manda un mensaje directo a los miembros que se unan al servidor.
    - Nero anuncia cuando un miembro se va del servidor.
    - Nero asigna un rol del servidor a un miembro dada su reacción a alguno de los emojis de un mensaje fijado para asignar los roles.
## **Requerimientos**
Para poder ejecutar el código se necesitará lo siguiente:
- Python 3.8.0 o superior.
- `discord.py` 1.5.1 o superior.
- `discord-ext-menus` 1.0.0a o superior.

### Para instalar Python:
Descargar la última versión aquí: https://www.python.org/downloads/
### Para instalar `discord.py`
`pip install discord.py`
### Para instalar `discord-ext-menus`
`pip install git+https://github.com/Rapptz/discord-ext-menus`
## **En caso de querer utilizar como base**
En caso de querer utilizar este código como base para otro bot, se requere crear un archivo .env que utilizará `settings.py` para cargar cierta información que utiliza Nero. Dentro de este archivo deben estar las siguientes variables:
  - `TOKEN`: Es el token que genera discord para el bot.
  - `GUILD_ID`: Es el ID del servidor donde se utilizará el bot.
  - `OWNER_ID`: Es el ID del usuario de discord que creó el bot.
  - `LOG_CHANNEL_ID`: Es el ID del canal que se utiliza para que Nero muestre información de ciertas acciones. Por ejemplo: información de baneos, notificar que está en línea, etc.
  - `WELCOME_CHANNEL_ID`: Es el ID del canal de bienvenida en el servidor, donde Nero saluda a los nuevos miembros y despide a los que se van.
  - `ROLES_CHANNEL_ID`: Es el ID del canal donde se fija el mensaje con las reacciones para seleccionar un rol.
  - `REACTION_MESSAGE_ID`: Es el ID del mensaje mencionado anteriormente.
  - `WELCOME_ROLE_ID`: Es el ID del rol de "inicio" que se asigna en el servidor, este se cambiará una vez se reaccione al mensaje para asignar un rol.

  Así mismo, tener en cuenta las restricciones de la licencia ligada a este repositorio.