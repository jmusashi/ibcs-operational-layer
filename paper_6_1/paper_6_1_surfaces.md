# Paper 6.1 — Surface Mapping

This document defines the operational representation of surfaces (M0) as
implemented in `mapping_surfaces.py`.

## What is a Surface
A surface is any observable interface where cognition interacts with the
environment. Examples include:

- Browser tabs
- Terminal sessions
- Repository files
- Simulation dashboards

## Surface Registry
Surfaces are registered in `SurfaceRegistry`, allowing the continuity engine
to track interactions across tools and contexts.

## Surface Metadata
Each surface includes:

- Name
- Type
- Metadata dictionary

This metadata enables cross-surface continuity.
