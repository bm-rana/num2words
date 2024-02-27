# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words


class Num2WordsARTest(TestCase):

    def test_default_currency(self):
        self.assertEqual(num2words(1, to='currency', lang='ar', rafea=True), 'واحد ريال')
        self.assertEqual(num2words(2, to='currency', lang='ar', rafea=True),
                         'اثنان ريالان')
        self.assertEqual(num2words(2, to='currency', lang='ar', rafea=False),
                         'اثنين ريالين')
        self.assertEqual(num2words(10, to='currency', lang='ar', rafea=True),
                         'عشرة ريالات')
        self.assertEqual(num2words(100, to='currency', lang='ar', rafea=True), 'مائة ريال')
        self.assertEqual(num2words(652.12, to='currency', lang='ar', rafea=True),
                         'ستمائة و اثنان و خمسون ريالاً و اثنتا عشرة هللة')
        self.assertEqual(num2words(324, to='currency', lang='ar', rafea=True),
                         'ثلاثمائة و أربعة و عشرون ريالاً')
        self.assertEqual(num2words(2000, to='currency', lang='ar', rafea=True),
                         'ألفا ريال')
        self.assertEqual(num2words(541, to='currency', lang='ar', rafea=True),
                         'خمسمائة و واحد و أربعون ريالاً')
        self.assertEqual(num2words(10000, to='currency', lang='ar', rafea=True),
                         'عشرة آلاف ريال')
        self.assertEqual(num2words(20000.12, to='currency', lang='ar', rafea=True),
                         'عشرون ألف ريال و اثنتا عشرة هللة')
        self.assertEqual(num2words(1000000, to='currency', lang='ar', rafea=True),
                         'مليون ريال')
        val = 'تسعمائة و ثلاثة و عشرون ألفاً و أربعمائة و أحد عشر ريالاً'
        self.assertEqual(num2words(923411, to='currency', lang='ar', rafea=True), val)
        self.assertEqual(num2words(63411, to='currency', lang='ar', rafea=True),
                         'ثلاثة و ستون ألفاً و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(num2words(1000000.99, to='currency', lang='ar', rafea=True),
                         'مليون ريال و تسع و تسعون هللة')

    def test_currency_parm(self):
        self.assertEqual(
            num2words(1, to='currency', lang='ar', currency="KWD", rafea=True),
            'واحد دينار')
        self.assertEqual(
            num2words(10, to='currency', lang='ar', currency="EGP", rafea=True),
            'عشرة جنيهات')
        self.assertEqual(
            num2words(20000.12, to='currency', lang='ar', currency="EGP", rafea=True),
            'عشرون ألف جنيه و اثنتا عشرة قرش')
        self.assertEqual(
            num2words(923411, to='currency', lang='ar', currency="SR", rafea=True),
            'تسعمائة و ثلاثة و عشرون ألفاً و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(
            num2words(1000000.99, to='currency', lang='ar', currency="KWD", rafea=True),
            'مليون دينار و تسع و تسعون فلس')

    def test_ordinal(self):

        self.assertEqual(num2words(1, to='ordinal', lang='ar', rafea=True), 'اول')
        self.assertEqual(num2words(2, to='ordinal', lang='ar', rafea=True), 'ثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='ar', rafea=True), 'ثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='ar', rafea=True), 'رابع')
        self.assertEqual(num2words(5, to='ordinal', lang='ar', rafea=True), 'خامس')
        self.assertEqual(num2words(6, to='ordinal', lang='ar', rafea=True), 'سادس')
        self.assertEqual(num2words(9, to='ordinal', lang='ar', rafea=True), 'تاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='ar', rafea=True), 'عشرون')
        self.assertEqual(num2words(94, to='ordinal', lang='ar', rafea=True),
                         'أربع و تسعون')
        self.assertEqual(num2words(102, to='ordinal', lang='ar', rafea=True),
                         'مائة و اثنان')
        self.assertEqual(
            num2words(923411, to='ordinal_num', lang='ar', rafea=True),
            'تسعمائة و ثلاثة و عشرون ألفاً و أربعمائة و أحد عشر')

        # See https://github.com/savoirfairelinux/num2words/issues/403
        self.assertEqual(num2words(23, lang="ar", rafea=True), 'ثلاثة و عشرون')
        self.assertEqual(num2words(23, to='ordinal',
                         lang="ar", rafea=True), 'ثلاث و عشرون')
        self.assertEqual(num2words(23, lang="ar", rafea=True), 'ثلاثة و عشرون')

    def test_cardinal(self):
        self.assertEqual(num2words(0, to='cardinal', lang='ar', rafea=True), 'صفر')
        self.assertEqual(num2words(12, to='cardinal', lang='ar', rafea=True), 'اثنا عشر')
        self.assertEqual(num2words(12.3, to='cardinal', lang='ar', rafea=True),
                         'اثنا عشر  , ثلاثون')
        self.assertEqual(num2words(12.01, to='cardinal', lang='ar', rafea=True),
                         'اثنا عشر  , إحدى')
        self.assertEqual(num2words(12.02, to='cardinal', lang='ar', rafea=True),
                         'اثنا عشر  , اثنتان')
        self.assertEqual(num2words(12.03, to='cardinal', lang='ar', rafea=True),
                         'اثنا عشر  , ثلاث')
        self.assertEqual(num2words(12.34, to='cardinal', lang='ar', rafea=True),
                         'اثنا عشر  , أربع و ثلاثون')
        # Not implemented
        self.assertEqual(num2words(12.345, to='cardinal', lang='ar', rafea=True),
                         num2words(12.34, to='cardinal', lang='ar', rafea=True))
        self.assertEqual(num2words(-8324, to='cardinal', lang='ar', rafea=True),
                         'سالب ثمانية آلاف و ثلاثمائة و أربعة و عشرون')

        self.assertEqual(num2words(200, to='cardinal', lang='ar', rafea=True),
                         'مئتا')
        self.assertEqual(num2words(700, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة')
        self.assertEqual(num2words(101010, to='cardinal', lang='ar', rafea=True),
                         'مائة و ألف ألف و عشرة')

        self.assertEqual(
            num2words(3431.12, to='cardinal', lang='ar', rafea=True),
            'ثلاثة آلاف و أربعمائة و واحد و ثلاثون  , اثنتا عشرة')
        self.assertEqual(num2words(431, to='cardinal', lang='ar', rafea=True),
                         'أربعمائة و واحد و ثلاثون')
        self.assertEqual(num2words(94231, to='cardinal', lang='ar', rafea=True),
                         'أربعة و تسعون ألفاً و مئتان و واحد و ثلاثون')
        self.assertEqual(num2words(1431, to='cardinal', lang='ar', rafea=True),
                         'ألف و أربعمائة و واحد و ثلاثون')
        self.assertEqual(num2words(740, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة و أربعون')
        self.assertEqual(num2words(741, to='cardinal', lang='ar', rafea=True),
                         # 'سبعة مائة و واحد و أربعون'
                         'سبعمائة و واحد و أربعون'
                         )
        self.assertEqual(num2words(262, to='cardinal', lang='ar', rafea=True),
                         'مئتان و اثنان و ستون'
                         )
        self.assertEqual(num2words(798, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة و ثمانية و تسعون'
                         )
        self.assertEqual(num2words(710, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة و عشرة')
        self.assertEqual(num2words(711, to='cardinal', lang='ar', rafea=True),
                         # 'سبعة مائة و إحدى عشر'
                         'سبعمائة و أحد عشر'
                         )
        self.assertEqual(num2words(700, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة')
        self.assertEqual(num2words(701, to='cardinal', lang='ar', rafea=True),
                         'سبعمائة و واحد')

        self.assertEqual(
            num2words(1258888, to='cardinal', lang='ar', rafea=True),
            'مليون و مئتان و ثمانية و خمسون ألفاً و ثمانمائة و ثمانية و ثمانون'
        )

        self.assertEqual(num2words(1100, to='cardinal', lang='ar', rafea=True),
                         'ألف و مائة')

        self.assertEqual(num2words(1000000521, to='cardinal', lang='ar', rafea=True),
                         'مليار و خمسمائة و واحد و عشرون')

    def test_prefix_and_suffix(self):
        self.assertEqual(num2words(645, to='currency',
                                   lang='ar', rafea=True, prefix="فقط", suffix="لاغير"),
                         'فقط ستمائة و خمسة و أربعون ريالاً لاغير')

    def test_year(self):
        self.assertEqual(num2words(2000, to='year', lang='ar', rafea=True), 'ألفا')

    def test_max_numbers(self):

        for number in 10**51, 10**51 + 2:

            with self.assertRaises(OverflowError) as context:
                num2words(number, lang='ar', rafea=True)

            self.assertTrue('must be less' in str(context.exception))

    def test_big_numbers(self):
        self.assertEqual(
            num2words(1000000045000000000000003000000002000000300,
                      to='cardinal', lang='ar',rafea=True),
            'تريديسيليون و خمسة و أربعون ديسيليوناً\
 و ثلاثة كوينتليونات و ملياران و ثلاثمائة'
        )
        self.assertEqual(
            num2words(-1000000000000000000000003000000002000000302,
                      to='cardinal', lang='ar', rafea=True),
            'سالب تريديسيليون و ثلاثة كوينتليونات \
و ملياران و ثلاثمائة و اثنان'
        )
        self.assertEqual(
            num2words(9999999999999999999999999999999999999999999999992,
                      to='cardinal', lang='ar', rafea=True),
            'تسعة كوينتينيليونات و تسعمائة و\
 تسعة و تسعون كوادريسيليوناً و تسعمائة و تسعة\
 و تسعون تريديسيليوناً و تسعمائة و تسعة و تسعون دوديسيليوناً و تسعمائة\
 و تسعة و تسعون أندسيليوناً و تسعمائة و تسعة و تسعون ديسيليوناً\
 و تسعمائة و تسعة و تسعون نونيليوناً و تسعمائة و تسعة و تسعون\
 أوكتيليوناً و تسعمائة و تسعة و تسعون سبتيليوناً و تسعمائة و تسعة\
 و تسعون سكستيليوناً و تسعمائة و تسعة و تسعون كوينتليوناً و تسعمائة و\
 تسعة و تسعون كوادريليوناً و تسعمائة و تسعة و تسعون تريليوناً\
 و تسعمائة و تسعة و تسعون ملياراً و تسعمائة و تسعة و تسعون مليوناً\
 و تسعمائة و تسعة و تسعون ألفاً و تسعمائة و اثنان و تسعون'
        )
