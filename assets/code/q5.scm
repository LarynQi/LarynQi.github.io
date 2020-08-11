; Q5a:
;
; Implement the append-stream procedure, which takes in two streams and returns a
; stream with the two streams concatenated. (Note that if the first stream is infinite,
; the result will not contain any elements from the second stream.)
; 
; Q5a - append-stream
;;; Tests
; (define s (cons-stream 1 (cons-stream 2 nil)))
; expect s
; (define a (append-stream s s))
; expect a
; (car (append-stream s s))
; expect 1
; (car (cdr-stream (append-stream s s)))
; expect 2
; (car (cdr-stream (cdr-stream (append-stream s s))))
; expect 1
; (car (cdr-stream (cdr-stream (cdr-stream (append-stream s s)))))
; expect 2
; (cdr-stream (cdr-stream (cdr-stream (cdr-stream (append-stream s s)))))
; expect ()

(define (append-stream s1 s2)
  'YOUR-CODE-HERE
)

; For testing purposes only:
(define s (cons-stream 1 (cons-stream 2 nil)))

; Q5b:
; 
; Now implement subset-stream, which takes in a normal Scheme list and returns a
; stream with every possible subset of that Scheme list.
; It might help to use map-stream, which we’ve defined for you below.
;
; Q5b - map-stream
;;; Tests
; (define a (subset-stream '(1 2 3 4 5)))
; expect a
; (car a)
; expect (1 2 3 4 5)
; (car (cdr-stream a))
; expect (1 2 3 4)
; (car (cdr-stream (cdr-stream a)))
; expect (1 2 3 5)
; (car (cdr-stream (cdr-stream (cdr-stream a))))
; expect (1 2 3)

(define (map-stream f s)
  (if (null? s)
    nil
    (cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define (subset-stream lst)
  'YOUR-CODE-HERE
)

; For testing purposes only:
(define a (subset-stream '(1 2 3 4 5)))
