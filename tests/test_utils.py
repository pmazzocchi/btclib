#!/usr/bin/env python3

# Copyright (C) 2017-2020 The btclib developers
#
# This file is part of btclib. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution.
#
# No part of btclib including this file, may be copied, modified, propagated,
# or distributed except according to the terms contained in the LICENSE file.

import unittest

from btclib.utils import h160h256, h256h256


class TestUtils(unittest.TestCase):

    def test_utils(self):
        s = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"
        self.assertEqual(h160h256(s), h160h256(bytes.fromhex(s)))
        self.assertEqual(h256h256(s), h256h256(bytes.fromhex(s)))


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
