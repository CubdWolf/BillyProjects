#!/usr/bin/racket
#lang racket

(require 2htdp/image)

(define CUTOFF 2)


(rectangle 2 3 "solid" "red")

#|
(define (scarpet s)
    (if (<= s CUTOFF)
        (square s "outline" "red")
        ()

|#