# Vouchers and discount codes

Vouchers and discount codes are two different ways to make
registrations cheaper or free for attendees. These can both be for
marketing purposes from the conference, as sponsor benefits, or as
almost anything.

## Prepaid vouchers

Prepaid vouchers are used to cover an entire registration. They are
locked to one specific registration type. The voucher code is sent to
the attendee, and the attendee performs their own registration and
puts this secret key in the voucher field, which makes the
registration free.

If all that's wanted is to register for another user, it's better to
use the [advanced registration flow](registrations). Vouchers are
appropriate if the vouchers are distributed to a different
organisation, and where the person paying does not have access to the
information about the attendee.

When creating vouchers, a *prepaid batch* is created, which contains a
certain number of vouchers. The batch is paid, and the usage of
vouchers can be tracked at this level.

## Discount codes

Discount codes are used to give a discount on a registration, but not
a free one. They can either be percentage based (in which case it can
either be a percentage of the registration cost alone, or a percentage
of the registration cost together with any additional options
selected) or a fixed amount.

When making a registration, discount codes are added to the same field
as voucher code, meaning the same registration cannot use both a
voucher and a discount code at the same time.

Discount codes can be limited to only be available for certain
registration types, or to require certain additional option (e.g. "you
get 20% off the main registration if you sign up for training
X"). They can have a maximum number of uses, and a final date on which
they can be used (e.g. the typical EARLYBIRD use).

## Reference

### Discount codes <a name="discountcodes"></a>

Code
: This is the actual code that should be entered.

Discountpercentage
: The percent discount that this code gives. Can't be specified at
the same time as discountamount.

Regonly
: The percent applies only to the registration, not the full cost
including additional options (only available if the type of
discount code is percentage)

Discountamount
: The amount of discount this code gives. Can't be specified at the
same time as discountpercentage.

Validuntil
: The date until which this code can be used.

Maxuses
: Maximum number of uses of this code.

Requiresregtype
: In order to use this discount code, one of the selected registration
types must be used.

Requiresoption
: In order to use this discount code, one of the selected additional
options have to be added to the registration.
