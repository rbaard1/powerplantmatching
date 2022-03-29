#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:48:04 2020

@author: fabian
"""

import pytest

import powerplantmatching as pm
from powerplantmatching import data

config = pm.get_config()
sources = config["matching_sources"]


@pytest.mark.parametrize("source", sources)
def test_data_request_raw(source):
    func = getattr(data, source)
    df = func(update=True, raw=True)
    if source == "OPSD":
        assert len(df["DE"])
        assert len(df["EU"])
    elif source == "GEO":
        assert len(df["Units"])
        assert len(df["Plants"])
    else:
        assert len(df)


@pytest.mark.parametrize("source", sources)
def test_data_request_processed(source):
    func = getattr(data, source)
    df = func()
    assert len(df)


def test_powerplants():
    pm.powerplants(from_url=True)
