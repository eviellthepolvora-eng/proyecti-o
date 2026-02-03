# Planificador de Entregas / Inventario (Proyecto adaptado)

Dominio: Tienda y distribución de motos (gestión de facturas y entregas).

Resumen rápido
- Eventos: facturas con una fecha (tupla día/mes/año) y datos del cliente.
- Recursos: `transportistas` (repartidores) , el `almacén` de modelos de moto , cliente (no participa directamente , solo brinda sus datos)
- Restricciones implementadas:
  - Máximo 3 entregas por día (controlado en `impor.eventoun.repeticion`).
  - Recursos limitados: número de transportistas y stock en `almacen.json`.

Archivos principales
- `el_inicio.py`: interfaz CLI principal (listar, agregar, eliminar,persistencia , filtrar ,ver inventario , crear inventario).
- `impor.py`: gestión de eventos (leer/escribir `eventos.json`).
- `transporte.py`: asignación de transportistas y registro de entregas `entregado.json`.
- `almacen_clases.py`: inventario, ajustes de entregas y alertas de stock bajo.
- 'factura_PERFECTA : evento principal del proyecto
- 'todo_relacionado_con_fecha : en los inicios fue el calendario principal pero luego de agregar la restriccion de buscar hueco para evitar errores se decide pasar a usar la libreria datatime

Persistencia
- `eventos.json`: eventos/facturas pendientes.
- `entregado.json`: bitácora de entregas realizadas.
- `almacen.json`: inventario actual.

Librerias
- `json` : facilitar el almacenamiento de datos
- `datatime ` : facilidades en metodos de busqueda de fechas libres

Cómo ejecutar
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:
```bash
python el_inicio.py
```

Notas
- `almacen_clases.almacenado()` permite crear/actualizar inventario.
- Se recomienda revisar y limpiar los JSON existentes si se migran datos.

Mejoras Posibles :
Cambiar la interfaz a una pagina web
Agregar mas recursos (carros , bicicletas , aviones , barcos) , mas detallez de los recursos (color ,clasificacion por estrellas)
Habilitar gps para direccion 