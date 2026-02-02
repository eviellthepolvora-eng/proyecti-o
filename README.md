# Planificador de Entregas / Inventario (Proyecto adaptado)

Dominio: Tienda y distribución de motos (gestión de facturas y entregas).

Resumen rápido
- Eventos: facturas con una fecha (tupla día/mes/año) y datos del cliente.
- Recursos: `transportistas` (repartidores) y el `almacén` de modelos de moto.
- Restricciones implementadas:
  - Máximo 3 entregas por día (controlado en `impor.eventoun.repeticion`).
  - Recursos limitados: número de transportistas y stock en `almacen.json`.

Archivos principales
- `el_inicio.py`: interfaz CLI principal (listar, agregar, eliminar,persistencia , filtrar ,ver inventario).
- `impor.py`: gestión de eventos (leer/escribir `eventos.json`).
- `transporte.py`: asignación de transportistas y registro de entregas `entregado.json`.
- `almacen_clases.py`: inventario, aplicar entregas y alertas de stock bajo.

Persistencia
- `eventos.json`: eventos/facturas pendientes.
- `entregado.json`: bitácora de entregas realizadas.
- `almacen.json`: inventario actual.

Cómo ejecutar
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:
```bash
python el_inicio.py
```

Notas y mejoras posibles
- `almacen_clases.almacenado()` permite crear/actualizar inventario.
- Se recomienda revisar y limpiar los JSON existentes si se migran datos.
