#!/usr/bin/env python3

# Copyright (C) 2017-2019 The btclib developers
#
# This file is part of btclib. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution.
#
# No part of btclib including this file, may be copied, modified, propagated,
# or distributed except according to the terms contained in the LICENSE file.

from btclib.ec import sha256, Scalar, Point, EllipticCurve, secp256k1, \
    DblScalarMult, secondGenerator


def pedersen_commit(r: Scalar,
                    v: Scalar,
                    ec: EllipticCurve = secp256k1,
                    hf = sha256) -> Point:
    # rG + vH
    H = secondGenerator(ec, hf)
    Q = DblScalarMult(ec, r, ec.G, v, H)
    assert Q is not None, "failed"
    return Q


def pedersen_open(r: Scalar,
                  v: Scalar,
                  C: Point,
                  ec: EllipticCurve = secp256k1,
                  hf = sha256) -> bool:
    return C == pedersen_commit(r, v, ec, hf)