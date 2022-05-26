#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LTE top level flowgraph SISO
# Author: Johannes Demel
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import lte
from lte_bch_decoder import lte_bch_decoder  # grc-generated hier_block
from lte_channel_estimator import lte_channel_estimator  # grc-generated hier_block
from lte_cp_ffo_sync import lte_cp_ffo_sync  # grc-generated hier_block
from lte_ofdm_demodulator import lte_ofdm_demodulator  # grc-generated hier_block
from lte_pbch_decoder import lte_pbch_decoder  # grc-generated hier_block
from lte_pcfich_decoder import lte_pcfich_decoder  # grc-generated hier_block
from lte_pss_sync import lte_pss_sync  # grc-generated hier_block
from lte_sss_sync import lte_sss_sync  # grc-generated hier_block



from gnuradio import qtgui

class lte_top_block_siso(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LTE top level flowgraph SISO", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LTE top level flowgraph SISO")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lte_top_block_siso")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.fftlen = fftlen = 2048
        self.samp_rate = samp_rate = (7*fftlen + 160* fftlen/2048 + 6 * (144 * fftlen/2048)) / 0.0005
        self.pbch_descr_key = pbch_descr_key = "descr_part"
        self.frame_key = frame_key = "slot"
        self.N_rb_dl = N_rb_dl = 6

        ##################################################
        # Blocks
        ##################################################
        self.sync_lte_rough_symbol_sync_cc_0 = lte.rough_symbol_sync_cc(fftlen, 1, "$id")
        self.pre_blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/johannes/src/gr-lte/tests/lte_test_data_RX1_NRBDL100.dat', True, 0, 0)
        self.pre_blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.lte_sss_sync_0 = lte_sss_sync(
            N_rb_dl=N_rb_dl,
            fftlen=fftlen,
            group_key="N_id_2",
            offset_key="offset_marker",
        )
        self.lte_pss_sync_0 = lte_pss_sync(
            fftlen=fftlen,
        )
        self.lte_pcfich_decoder_0 = lte_pcfich_decoder(
            N_rb_dl=N_rb_dl,
            key="slot",
        )
        self.lte_pbch_decoder_0 = lte_pbch_decoder(
            N_rb_dl=50,
        )
        self.lte_ofdm_demodulator_0 = lte_ofdm_demodulator(
            N_rb_dl=N_rb_dl,
            fftlen=fftlen,
            ofdm_key="slot",
        )
        self.lte_cp_ffo_sync_0 = lte_cp_ffo_sync(
            fftlen=fftlen,
        )
        self.lte_channel_estimator_0 = lte_channel_estimator(
            N_rb_dl=N_rb_dl,
            estimator_key="slot",
            initial_id=124,
        )
        self.lte_bch_decoder_0 = lte_bch_decoder()
        self.MIB = lte.mib_unpack_vbm("$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.MIB, 'N_ant'), (self.lte_pcfich_decoder_0, 'N_ant'))
        self.msg_connect((self.lte_sss_sync_0, 'cell_id'), (self.lte_channel_estimator_0, 'cell_id'))
        self.msg_connect((self.lte_sss_sync_0, 'cell_id'), (self.lte_pbch_decoder_0, 'cell_id'))
        self.msg_connect((self.lte_sss_sync_0, 'cell_id'), (self.lte_pcfich_decoder_0, 'cell_id'))
        self.connect((self.lte_bch_decoder_0, 1), (self.MIB, 1))
        self.connect((self.lte_bch_decoder_0, 0), (self.MIB, 0))
        self.connect((self.lte_channel_estimator_0, 0), (self.lte_pbch_decoder_0, 1))
        self.connect((self.lte_channel_estimator_0, 1), (self.lte_pbch_decoder_0, 2))
        self.connect((self.lte_channel_estimator_0, 0), (self.lte_pcfich_decoder_0, 1))
        self.connect((self.lte_channel_estimator_0, 1), (self.lte_pcfich_decoder_0, 2))
        self.connect((self.lte_cp_ffo_sync_0, 0), (self.lte_sss_sync_0, 0))
        self.connect((self.lte_ofdm_demodulator_0, 0), (self.lte_channel_estimator_0, 0))
        self.connect((self.lte_ofdm_demodulator_0, 0), (self.lte_pbch_decoder_0, 0))
        self.connect((self.lte_ofdm_demodulator_0, 0), (self.lte_pcfich_decoder_0, 0))
        self.connect((self.lte_pbch_decoder_0, 0), (self.lte_bch_decoder_0, 0))
        self.connect((self.lte_pss_sync_0, 0), (self.lte_cp_ffo_sync_0, 0))
        self.connect((self.lte_sss_sync_0, 0), (self.lte_ofdm_demodulator_0, 0))
        self.connect((self.pre_blocks_file_source_0, 0), (self.sync_lte_rough_symbol_sync_cc_0, 0))
        self.connect((self.sync_lte_rough_symbol_sync_cc_0, 0), (self.lte_pss_sync_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lte_top_block_siso")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen
        self.set_samp_rate((7*self.fftlen + 160* self.fftlen/2048 + 6 * (144 * self.fftlen/2048)) / 0.0005)
        self.lte_cp_ffo_sync_0.set_fftlen(self.fftlen)
        self.lte_ofdm_demodulator_0.set_fftlen(self.fftlen)
        self.lte_pss_sync_0.set_fftlen(self.fftlen)
        self.lte_sss_sync_0.set_fftlen(self.fftlen)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_pbch_descr_key(self):
        return self.pbch_descr_key

    def set_pbch_descr_key(self, pbch_descr_key):
        self.pbch_descr_key = pbch_descr_key

    def get_frame_key(self):
        return self.frame_key

    def set_frame_key(self, frame_key):
        self.frame_key = frame_key

    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl
        self.lte_channel_estimator_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_ofdm_demodulator_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_pcfich_decoder_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_sss_sync_0.set_N_rb_dl(self.N_rb_dl)




def main(top_block_cls=lte_top_block_siso, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
