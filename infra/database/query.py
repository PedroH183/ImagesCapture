get_all_files = """
    select
        *
    from files order by created_at;
"""

ins_informations_captured = """
    insert into
        products_captured(product_title, product_link_image)
    values (
        %(product_title)s, %(product_link_image)s
    );
"""