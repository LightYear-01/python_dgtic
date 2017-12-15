#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT


def palindromo(cadena):
	if cadena == cadena[::-1]:
		return True
	else:
		return False
