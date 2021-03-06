from django import test
from django.conf import settings
from django_2gis_maps.widgets import DoubleGisMapsAddressWidget


class WidgetTests(test.TestCase):
    def test_render_returns_xxxxxxx(self):
        widget = DoubleGisMapsAddressWidget()
        results = widget.render('name', 'value', attrs={'a1': 1, 'a2': 2})
        expected = '<input a1="1" a2="2" name="name" type="text" value="value" />'
        expected += '<div class="map_canvas_wrapper">'
        expected += '<div id="map_canvas"></div></div>'
        self.assertHTMLEqual(expected, results)

    def test_render_returns_blank_for_value_when_none(self):
        widget = DoubleGisMapsAddressWidget()
        results = widget.render('name', None, attrs={'a1': 1, 'a2': 2})
        expected = '<input a1="1" a2="2" name="name" type="text" />'
        expected += '<div class="map_canvas_wrapper">'
        expected += '<div id="map_canvas"></div></div>'
        self.assertHTMLEqual(expected, results)

    def test_maps_js_uses_api_key(self):
        widget = DoubleGisMapsAddressWidget()
        django_2gis_maps_js = "https://maps.api.2gis.ru/2.0/loader.js?pkg=full&skin=dark"
        self.assertEqual(django_2gis_maps_js, widget.Media().js[1])
