from typing import Any, Callable, Literal

from pydantic import validate_arguments

import mesop.components.input.input_pb2 as input_pb
from mesop.component_helpers import (
  handler_type,
  insert_component,
)
from mesop.events import InputEvent


@validate_arguments
def input(
  *,
  key: str | None = None,
  disabled: bool = False,
  id: str = "",
  placeholder: str = "",
  name: str = "",
  required: bool = False,
  type: str = "",
  user_aria_described_by: str = "",
  value: str = "",
  readonly: bool = False,
  hide_required_marker: bool = False,
  color: Literal["primary", "accent", "warn"] = "primary",
  float_label: Literal["always", "auto"] = "auto",
  appearance: Literal["fill", "outline"] = "fill",
  subscript_sizing: Literal["fixed", "dynamic"] = "fixed",
  hint_label: str = "",
  label: str = "",
  on_input: Callable[[InputEvent], Any] | None = None,
  variant: Literal["matInput"] = "matInput",
):
  """Creates a Input component.

  Args:
    key (str|None): Unique identifier for this component instance.
    disabled (bool): Implemented as part of MatFormFieldControl. @docs-private
    id (str): Implemented as part of MatFormFieldControl. @docs-private
    placeholder (str): Implemented as part of MatFormFieldControl. @docs-private
    name (str): Name of the input. @docs-private
    required (bool): Implemented as part of MatFormFieldControl. @docs-private
    type (str): Input type of the element.
    user_aria_described_by (str): Implemented as part of MatFormFieldControl. @docs-private
    value (str): Implemented as part of MatFormFieldControl. @docs-private
    readonly (bool): Whether the element is readonly.
    hide_required_marker (bool): Whether the required marker should be hidden.
    color (Literal['primary','accent','warn']): The color palette for the form field.
    float_label (Literal['always','auto']): Whether the label should always float or float as the user types.
    appearance (Literal['fill','outline']): The form field appearance style.
    subscript_sizing (Literal['fixed','dynamic']): Whether the form field should reserve space for one line of hint/error text (default) or to have the spacing grow from 0px as needed based on the size of the hint/error content. Note that when using dynamic sizing, layout shifts will occur when hint/error text changes.
    hint_label (str): Text for the form field hint.
    label (str):
    on_input (Callable[[InputEvent], Any]|None): [input](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event) is a native browser event.
    variant (Literal['matInput']): component variations
  """
  insert_component(
    key=key,
    type_name="input",
    proto=input_pb.InputType(
      disabled=disabled,
      id=id,
      placeholder=placeholder,
      name=name,
      required=required,
      type=type,
      user_aria_described_by=user_aria_described_by,
      value=value,
      readonly=readonly,
      hide_required_marker=hide_required_marker,
      color=color,
      float_label=float_label,
      appearance=appearance,
      subscript_sizing=subscript_sizing,
      hint_label=hint_label,
      label=label,
      on_input_handler_id=handler_type(on_input) if on_input else "",
      variant_index=_get_variant_index(variant),
    ),
  )


def _get_variant_index(variant: str) -> int:
  if variant == "matInput":
    return 0
  raise Exception("Unexpected variant: " + variant)