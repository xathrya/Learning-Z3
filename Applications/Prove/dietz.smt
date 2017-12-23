(declare-const x (_ BitVec 64))
(declare-const y (_ BitVec 64))
(assert
    (forall ((x (_ BitVec 64)) (y (_ BitVec 64)))
        (=
            ((_ zero_extend 1)
                (bvadd
                    (bvand x y)
                    (bvlshr (bvxor x y) (_ bv1 64))
                )
            )
            (bvlshr
                (bvadd ((_ zero_extend 1) x) ((_ zero_extend 1) y))
                (_ bv1 65)
            )
        )
    )
)
(check-sat)