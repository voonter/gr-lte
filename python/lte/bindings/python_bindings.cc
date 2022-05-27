/*
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include <pybind11/pybind11.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

namespace py = pybind11;

// Headers for binding functions
/**************************************/
// The following comment block is used for
// gr_modtool to insert function prototypes
// Please do not delete
/**************************************/
// BINDING_FUNCTION_PROTOTYPES(
void bind_bch_crc_check_ant_chooser_bb(py::module&);
void bind_channel_estimator_vcvc(py::module&);
void bind_crc_check_vbvb(py::module&);
void bind_descrambler_vfvf(py::module&);
void bind_extract_subcarriers_vcvc(py::module&);
void bind_layer_demapper_vcvc(py::module&);
void bind_mib_unpack_vbm(py::module&);
void bind_mimo_pss_coarse_control(py::module&);
void bind_mimo_pss_coarse_sync(py::module&);
void bind_mimo_pss_fine_sync(py::module&);
void bind_mimo_pss_freq_sync(py::module&);
void bind_mimo_pss_tagger(py::module&);
void bind_mimo_remove_cp(py::module&);
void bind_mimo_sss_calculator(py::module&);
void bind_mimo_sss_symbol_selector(py::module&);
void bind_mimo_sss_tagger(py::module&);
void bind_pbch_demux_vcvc(py::module&);
void bind_pbch_descrambler_vfvf(py::module&);
void bind_pcfich_demux_vcvc(py::module&);
void bind_pcfich_unpack_vfm(py::module&);
void bind_pre_decoder_vcvc(py::module&);
void bind_pss_calculator_vcm(py::module&);
void bind_pss_symbol_selector_cvc(py::module&);
void bind_pss_tagger_cc(py::module&);
void bind_qpsk_soft_demod_vcvf(py::module&);
void bind_remove_cp_cvc(py::module&);
void bind_repeat_message_source_vf(py::module&);
void bind_rough_symbol_sync_cc(py::module&);
void bind_sss_calculator_vcm(py::module&);
void bind_sss_symbol_selector_cvc(py::module&);
void bind_sss_tagger_cc(py::module&);
void bind_subblock_deinterleaver_vfvf(py::module&);
void bind_sync_frequency_c(py::module&);
// ) END BINDING_FUNCTION_PROTOTYPES


// We need this hack because import_array() returns NULL
// for newer Python versions.
// This function is also necessary because it ensures access to the C API
// and removes a warning.
void* init_numpy()
{
    import_array();
    return NULL;
}

PYBIND11_MODULE(lte_python, m)
{
    // Initialize the numpy C API
    // (otherwise we will see segmentation faults)
    init_numpy();

    // Allow access to base block methods
    py::module::import("gnuradio.gr");

    /**************************************/
    // The following comment block is used for
    // gr_modtool to insert binding function calls
    // Please do not delete
    /**************************************/
    // BINDING_FUNCTION_CALLS(
    bind_bch_crc_check_ant_chooser_bb(m);
    bind_channel_estimator_vcvc(m);
    bind_crc_check_vbvb(m);
    bind_descrambler_vfvf(m);
    bind_extract_subcarriers_vcvc(m);
    bind_layer_demapper_vcvc(m);
    bind_mib_unpack_vbm(m);
    bind_mimo_pss_coarse_control(m);
    bind_mimo_pss_coarse_sync(m);
    bind_mimo_pss_fine_sync(m);
    bind_mimo_pss_freq_sync(m);
    bind_mimo_pss_tagger(m);
    bind_mimo_remove_cp(m);
    bind_mimo_sss_calculator(m);
    bind_mimo_sss_symbol_selector(m);
    bind_mimo_sss_tagger(m);
    bind_pbch_demux_vcvc(m);
    bind_pbch_descrambler_vfvf(m);
    bind_pcfich_demux_vcvc(m);
    bind_pcfich_unpack_vfm(m);
    bind_pre_decoder_vcvc(m);
    bind_pss_calculator_vcm(m);
    bind_pss_symbol_selector_cvc(m);
    bind_pss_tagger_cc(m);
    bind_qpsk_soft_demod_vcvf(m);
    bind_remove_cp_cvc(m);
    bind_repeat_message_source_vf(m);
    bind_rough_symbol_sync_cc(m);
    bind_sss_calculator_vcm(m);
    bind_sss_symbol_selector_cvc(m);
    bind_sss_tagger_cc(m);
    bind_subblock_deinterleaver_vfvf(m);
    bind_sync_frequency_c(m);
    // ) END BINDING_FUNCTION_CALLS
}
