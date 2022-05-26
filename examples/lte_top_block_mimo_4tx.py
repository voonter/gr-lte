#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MIMO TOP FLOW 4 Tx ant
# Author: Kristian Maier, Johannes Demel
# Description: LTE decoding up to 4 tx antennas
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
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import lte
from lte_bch_decoder import lte_bch_decoder  # grc-generated hier_block
from lte_channel_estimator_mimo_4tx import lte_channel_estimator_mimo_4tx  # grc-generated hier_block
from lte_ofdm_demodulator_mimo_2tx import lte_ofdm_demodulator_mimo_2tx  # grc-generated hier_block
from lte_pbch_decoder_mimo_4tx import lte_pbch_decoder_mimo_4tx  # grc-generated hier_block
from lte_pss_sync_direct_mimo_2tx import lte_pss_sync_direct_mimo_2tx  # grc-generated hier_block
from lte_sss_sync_freq_domain_mimo_2tx import lte_sss_sync_freq_domain_mimo_2tx  # grc-generated hier_block



from gnuradio import qtgui

class lte_top_block_mimo_4tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MIMO TOP FLOW 4 Tx ant", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MIMO TOP FLOW 4 Tx ant")
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

        self.settings = Qt.QSettings("GNU Radio", "lte_top_block_mimo_4tx")

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
        self.fftl = fftl = 1024
        self.samp_rate = samp_rate = fftl*15e3
        self.rxant = rxant = 2
        self.resampler = resampler = 400
        self.frame_key = frame_key = "slot"
        self.N_rb_dl = N_rb_dl = 50

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=1536*fftl//1024,
                decimation=resampler,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1536*fftl//1024,
                decimation=resampler,
                taps=[],
                fractional_bw=0)
        self.lte_sss_sync_freq_domain_mimo_2tx_0 = lte_sss_sync_freq_domain_mimo_2tx(
            N_rb_dl=N_rb_dl,
            rxant=rxant,
        )
        self.lte_pss_sync_direct_mimo_2tx_0 = lte_pss_sync_direct_mimo_2tx(
            fftlen=fftl,
            rxant=rxant,
            synclen=5,
        )
        self.lte_pbch_decoder_mimo_4tx_0 = lte_pbch_decoder_mimo_4tx(
            N_rb_dl=N_rb_dl,
            rxant=rxant,
        )
        self.lte_ofdm_demodulator_mimo_2tx_0 = lte_ofdm_demodulator_mimo_2tx(
            N_rb_dl=N_rb_dl,
            fftlen=fftl,
            ofdm_key="slot",
            rxant=rxant,
        )
        self.lte_channel_estimator_mimo_4tx_0 = lte_channel_estimator_mimo_4tx(
            N_rb_dl=N_rb_dl,
            estimator_key="slot",
            initial_id=333,
            rxant=rxant,
        )
        self.lte_bch_decoder_0 = lte_bch_decoder()
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*2, samp_rate,True)
        self.blocks_streams_to_vector_0_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*12 * N_rb_dl, 2)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*2, '/home/maier/LTE test files/live data/lte_capture_Wed_Aug_6_19:36:39_2014_RXant2_4MS_telekom_band1800_wg_karlruhe_hinten raus_messung1.dat', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.MIB = lte.mib_unpack_vbm("$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lte_pss_sync_direct_mimo_2tx_0, 'N_id_2'), (self.lte_sss_sync_freq_domain_mimo_2tx_0, 'N_id_2'))
        self.msg_connect((self.lte_sss_sync_freq_domain_mimo_2tx_0, 'cell_id'), (self.lte_channel_estimator_mimo_4tx_0, 'cell_id'))
        self.msg_connect((self.lte_sss_sync_freq_domain_mimo_2tx_0, 'cell_id'), (self.lte_pbch_decoder_mimo_4tx_0, 'cell_id'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.lte_channel_estimator_mimo_4tx_0, 0))
        self.connect((self.blocks_streams_to_vector_0_0, 0), (self.lte_pbch_decoder_mimo_4tx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.lte_bch_decoder_0, 1), (self.MIB, 1))
        self.connect((self.lte_bch_decoder_0, 0), (self.MIB, 0))
        self.connect((self.lte_channel_estimator_mimo_4tx_0, 2), (self.lte_pbch_decoder_mimo_4tx_0, 3))
        self.connect((self.lte_channel_estimator_mimo_4tx_0, 3), (self.lte_pbch_decoder_mimo_4tx_0, 4))
        self.connect((self.lte_channel_estimator_mimo_4tx_0, 1), (self.lte_pbch_decoder_mimo_4tx_0, 2))
        self.connect((self.lte_channel_estimator_mimo_4tx_0, 0), (self.lte_pbch_decoder_mimo_4tx_0, 1))
        self.connect((self.lte_ofdm_demodulator_mimo_2tx_0, 1), (self.lte_sss_sync_freq_domain_mimo_2tx_0, 1))
        self.connect((self.lte_ofdm_demodulator_mimo_2tx_0, 0), (self.lte_sss_sync_freq_domain_mimo_2tx_0, 0))
        self.connect((self.lte_pbch_decoder_mimo_4tx_0, 0), (self.lte_bch_decoder_0, 0))
        self.connect((self.lte_pss_sync_direct_mimo_2tx_0, 0), (self.lte_ofdm_demodulator_mimo_2tx_0, 0))
        self.connect((self.lte_pss_sync_direct_mimo_2tx_0, 1), (self.lte_ofdm_demodulator_mimo_2tx_0, 1))
        self.connect((self.lte_sss_sync_freq_domain_mimo_2tx_0, 0), (self.blocks_streams_to_vector_0_0, 0))
        self.connect((self.lte_sss_sync_freq_domain_mimo_2tx_0, 1), (self.blocks_streams_to_vector_0_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.lte_pss_sync_direct_mimo_2tx_0, 1))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.lte_pss_sync_direct_mimo_2tx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lte_top_block_mimo_4tx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_fftl(self):
        return self.fftl

    def set_fftl(self, fftl):
        self.fftl = fftl
        self.set_samp_rate(self.fftl*15e3)
        self.lte_ofdm_demodulator_mimo_2tx_0.set_fftlen(self.fftl)
        self.lte_pss_sync_direct_mimo_2tx_0.set_fftlen(self.fftl)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant
        self.lte_channel_estimator_mimo_4tx_0.set_rxant(self.rxant)
        self.lte_ofdm_demodulator_mimo_2tx_0.set_rxant(self.rxant)
        self.lte_pbch_decoder_mimo_4tx_0.set_rxant(self.rxant)
        self.lte_pss_sync_direct_mimo_2tx_0.set_rxant(self.rxant)
        self.lte_sss_sync_freq_domain_mimo_2tx_0.set_rxant(self.rxant)

    def get_resampler(self):
        return self.resampler

    def set_resampler(self, resampler):
        self.resampler = resampler

    def get_frame_key(self):
        return self.frame_key

    def set_frame_key(self, frame_key):
        self.frame_key = frame_key

    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl
        self.lte_channel_estimator_mimo_4tx_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_ofdm_demodulator_mimo_2tx_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_pbch_decoder_mimo_4tx_0.set_N_rb_dl(self.N_rb_dl)
        self.lte_sss_sync_freq_domain_mimo_2tx_0.set_N_rb_dl(self.N_rb_dl)




def main(top_block_cls=lte_top_block_mimo_4tx, options=None):

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
