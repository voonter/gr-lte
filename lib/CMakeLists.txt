# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

list(APPEND lte_sources
    mib_unpack_vbm_impl.cc
    crc_check_vbvb_impl.cc
    bch_crc_check_ant_chooser_bb_impl.cc
    subblock_deinterleaver_vfvf_impl.cc
    pbch_descrambler_vfvf_impl.cc
    repeat_message_source_vf_impl.cc
    qpsk_soft_demod_vcvf_impl.cc
    layer_demapper_vcvc_impl.cc
    pre_decoder_vcvc_impl.cc
    pbch_demux_vcvc_impl.cc
    channel_estimator_vcvc_impl.cc
    extract_subcarriers_vcvc_impl.cc
    remove_cp_cvc_impl.cc
    sss_calculator_vcm_impl.cc
    pcfich_unpack_vfm_impl.cc
    rough_symbol_sync_cc_impl.cc
    pss_symbol_selector_cvc_impl.cc
    pss_calculator_vcm_impl.cc
    pss_tagger_cc_impl.cc
    correlator_impl.cc
    sss_symbol_selector_cvc_impl.cc
    sss_tagger_cc_impl.cc
    sync_frequency_c_impl.cc
    descrambler_vfvf_impl.cc
    pcfich_demux_vcvc_impl.cc
    mimo_pss_coarse_sync_impl.cc
    mimo_pss_fine_sync_impl.cc
    mimo_pss_tagger_impl.cc
    mimo_pss_coarse_control_impl.cc
    pss_impl.cc
    mimo_pss_freq_sync_impl.cc
    mimo_sss_symbol_selector_impl.cc
    mimo_sss_calculator_impl.cc
    mimo_sss_tagger_impl.cc
    mimo_remove_cp_impl.cc )

set(lte_sources "${lte_sources}" PARENT_SCOPE)
if(NOT lte_sources)
    MESSAGE(STATUS "No C++ sources... skipping lib/")
    return()
endif(NOT lte_sources)

add_library(gnuradio-lte SHARED ${lte_sources})
target_link_libraries(gnuradio-lte PUBLIC gnuradio::gnuradio-runtime fftw3f::fftw3f Volk::volk)
target_include_directories(gnuradio-lte
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>
    PUBLIC $<INSTALL_INTERFACE:include>
  )
set_target_properties(gnuradio-lte PROPERTIES DEFINE_SYMBOL "gnuradio_lte_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-lte PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-lte)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

# If your unit tests require special include paths, add them here
#include_directories()
# List all files that contain Boost.UTF unit tests here
list(APPEND test_lte_sources
)
# Anything we need to link to for the unit tests go here
list(APPEND GR_TEST_TARGET_DEPS gnuradio-lte)

if(NOT test_lte_sources)
    MESSAGE(STATUS "No C++ unit tests... skipping")
    return()
endif(NOT test_lte_sources)

foreach(qa_file ${test_lte_sources})
    GR_ADD_CPP_TEST("lte_${qa_file}"
        ${CMAKE_CURRENT_SOURCE_DIR}/${qa_file}
    )
endforeach(qa_file)
