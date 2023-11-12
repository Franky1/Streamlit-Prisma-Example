# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template models.py.jinja --
import os
import logging
import inspect
import warnings
from collections import OrderedDict

from pydantic import BaseModel, Field

from . import types, enums, errors, fields, bases
from ._types import FuncType
from ._compat import model_rebuild, field_validator
from .builder import serialize_base64
from .generator import partial_models_ctx, PartialModelField


log: logging.Logger = logging.getLogger(__name__)
_created_partial_types: Set[str] = set()

class Post(bases.BasePost):
    """Represents a Post record"""

    id: _str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    author: Optional[_str] = None
    title: _str
    content: Optional[_str] = None

    # take *args and **kwargs so that other metaclasses can define arguments
    def __init_subclass__(
        cls,
        *args: Any,
        warn_subclass: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init_subclass__()
        if warn_subclass is not None:
            warnings.warn(
                'The `warn_subclass` argument is deprecated as it is no longer necessary and will be removed in the next release',
                DeprecationWarning,
                stacklevel=3,
            )


    @staticmethod
    def create_partial(
        name: str,
        include: Optional[Iterable['types.PostKeys']] = None,
        exclude: Optional[Iterable['types.PostKeys']] = None,
        required: Optional[Iterable['types.PostKeys']] = None,
        optional: Optional[Iterable['types.PostKeys']] = None,
        relations: Optional[Mapping['types.PostRelationalFieldKeys', str]] = None,
        exclude_relational_fields: bool = False,
    ) -> None:
        if not os.environ.get('PRISMA_GENERATOR_INVOCATION'):
            raise RuntimeError(
                'Attempted to create a partial type outside of client generation.'
            )

        if name in _created_partial_types:
            raise ValueError(f'Partial type "{name}" has already been created.')

        if include is not None:
            if exclude is not None:
                raise TypeError('Exclude and include are mutually exclusive.')
            if exclude_relational_fields is True:
                raise TypeError('Include and exclude_relational_fields=True are mutually exclusive.')

        if required and optional:
            shared = set(required) & set(optional)
            if shared:
                raise ValueError(f'Cannot make the same field(s) required and optional {shared}')

        if exclude_relational_fields and relations:
            raise ValueError(
                'exclude_relational_fields and relations are mutually exclusive'
            )

        fields: Dict['types.PostKeys', PartialModelField] = OrderedDict()

        try:
            if include:
                for field in include:
                    fields[field] = _Post_fields[field].copy()
            elif exclude:
                for field in exclude:
                    if field not in _Post_fields:
                        raise KeyError(field)

                fields = {
                    key: data.copy()
                    for key, data in _Post_fields.items()
                    if key not in exclude
                }
            else:
                fields = {
                    key: data.copy()
                    for key, data in _Post_fields.items()
                }

            if required:
                for field in required:
                    fields[field]['optional'] = False

            if optional:
                for field in optional:
                    fields[field]['optional'] = True


            if relations:
                raise ValueError('Model: "Post" has no relational fields.')
        except KeyError as exc:
            raise ValueError(
                f'{exc.args[0]} is not a valid Post / {name} field.'
            ) from None

        models = partial_models_ctx.get()
        models.append(
            {
                'name': name,
                'fields': cast(Mapping[str, PartialModelField], fields),
                'from_model': 'Post',
            }
        )
        _created_partial_types.add(name)



_Post_relational_fields: Set[str] = set()  # pyright: ignore[reportUnusedVariable]
_Post_fields: Dict['types.PostKeys', PartialModelField] = OrderedDict(
    [
        ('id', {
            'name': 'id',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('created_at', {
            'name': 'created_at',
            'is_list': False,
            'optional': False,
            'type': 'datetime.datetime',
            'is_relational': False,
            'documentation': None,
        }),
        ('updated_at', {
            'name': 'updated_at',
            'is_list': False,
            'optional': False,
            'type': 'datetime.datetime',
            'is_relational': False,
            'documentation': None,
        }),
        ('author', {
            'name': 'author',
            'is_list': False,
            'optional': True,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('title', {
            'name': 'title',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('content', {
            'name': 'content',
            'is_list': False,
            'optional': True,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
    ],
)



# we have to import ourselves as relation types are namespaced to models
# e.g. models.Post
from . import models, actions

# required to support relationships between models
model_rebuild(Post)
