from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.

    Example:
        >> flip_kv_vk({'tokyo': 'Токио', 'moscow': 'Москва'})
        {
            'Токио': 'tokyo',
            'Москва': 'moscow',
        }
    """
    keys = list(d.keys())
    values = list(d.values())
    return dict(zip(values, keys))


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - список ключей,
    конфликтующих значений.

    Example:
        >> flip_kv_vk({'Санкт-Петербург': '+3', 'Москва': '+3'})
        {
            '+3': ['Москва', 'Санкт-Петербург'],
        }
    """
    res_dict = dict()
    for k, v in d.items():
        if res_dict.__contains__(v):
            res_dict[v].append(k)
        else:
            res_dict[v] = [k]
    return res_dict
