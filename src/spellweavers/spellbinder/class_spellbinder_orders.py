from spellweavers.default.class_default_orders import DefaultOrder, DefaultOrders


class SpellbinderOrder(DefaultOrder):
    """Thin Spellbinder wrapper over Default Order."""


class SpellbinderOrders(DefaultOrders):
    """Thin Spellbinder wrapper over Default Orders."""

    order_class = SpellbinderOrder
