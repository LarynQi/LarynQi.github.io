; Q2:
;
; Write a function that takes a procedure and applies to every element in a given
; nested list.
; The result should be a nested list with the same structure as the input list, but
; with each element replaced by the result of applying the procedure to that element.
; Use the built-in list? procedure to detect whether a value is a list.
;
; Q2 - deep-map
;;; Tests
; (deep-map (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)
; (deep-map (lambda (x) (* x x)) '(1 ((4) 5) 9))
; expect (1 ((16) 25) 81)

(define (deep-map fn lst)
  (cond ((null? lst) lst)
        ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
        (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
        )
  )
